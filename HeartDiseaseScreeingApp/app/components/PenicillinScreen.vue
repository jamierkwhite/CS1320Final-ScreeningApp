<template>
    <Page class="page">
        <ActionBar title="Penicillin">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <!-- <RadDataForm :source="album" /> -->
        <StackLayout>
            <RadDataForm :source="patient" :metadata="patientMetadata"
                @propertyCommitted="onPropertyCommitted" />
            <Button text="Submit" @tap="onButtonTap" class="regsubmit" />
        </StackLayout>
    </Page>
</template>

<script>
    import Vue from "nativescript-vue";
    import RadDataForm from "nativescript-ui-dataform/vue";
    Vue.use(RadDataForm);

    export default {
        data() {
            return {
                patient: {
                    date: "",
                    location: "",
                    worsening_exercise_intolerance: "No",
                    poor_pcn_reaction: "No",
                    injection_given: "No",
                    comments: ""
                },
                patientMetadata: {
                    isReadOnly: false,
                    commitMode: "Immediate",
                    validationMode: "Immediate",
                    propertyAnnotations: [{
                            name: "date",
                            displayName: "Date",
                            index: 0,
                            editor: "Text",
                            readOnly: true
                        },
                        {
                            name: "location",
                            displayName: "Location",
                            index: 1,
                            editor: "Text"
                        },
                        {
                            name: "worsening_exercise_intolerance",
                            displayName: "Worsening Exercise Intolerance",
                            index: 2,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Yes", "No"]
                        },
                        {
                            name: "poor_pcn_reaction",
                            displayName: "Poor Penicillin Reaction",
                            index: 3,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Yes", "No"]
                        },
                        {
                            name: "injection_given",
                            displayName: "Injection Given",
                            index: 4,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Yes", "No"]
                        },
                        {
                            name: "comments",
                            displayName: "Comments",
                            index: 5,
                            editor: "MultilineText"
                        }
                    ]
                },
                committedPerson: {},
                today_date: ""
            };
        },
        beforeMount() {
            this.getDate();
        },
        methods: {
            onButtonTap() {
                console.log(this.committedPerson);
            },
            onPropertyCommitted(data) {
                this.committedPerson = data.object.editedObject;
            },
            getDate() {
                var today = new Date();
                var dd = today.getDate();
                var mm = today.getMonth() + 1;
                var yyyy = today.getFullYear();
                if (dd < 10) {
                    dd = "0" + dd;
                }
                if (mm < 10) {
                    mm = "0" + mm;
                }
                today = mm + "/" + dd + "/" + yyyy;
                this.today_date = today;
                this.patient.date = today;
            }
        }
    };
    //#34ebcf
</script>

<style scoped>
    DataFormEditorLabel {
        color: #212121;
        font-style: italic;
        font-weight: bold;
        font-size: 16;
        width: 160;
        textAlign: center;
    }

    DataFormEditorCore {
        margin: 5;
        padding: 5;
        border-color: darkgray;
        border-width: 2;
        border-radius: 5;
        font-size: 14;
    }

    PropertyEditor[type='SegmentedEditor'] DataFormEditorCore {
        border-width: 0;
        margin: 12;
    }

    PropertyEditor[type='MultilineText'] DataFormEditorCore {
        /* margin-top: 15;
        margin-bottom: 15; */
        margin-left: 0;
        margin-right: 0;
        padding-top: 50;
        padding-bottom: 50;
    }

    PropertyEditor[type='MultilineText'] DataFormEditorLabel {
        margin-top: 15;
        margin-bottom: 15;
        padding-top: 35;
        padding-bottom: 35;
    }

    .regsubmit {
        background-color: #24b39d;
        color: white;
        font-size: 16;
        font-weight: bold;
        width: 200;
        border-radius: 12px;
        margin-top: 20px;
    }
</style>