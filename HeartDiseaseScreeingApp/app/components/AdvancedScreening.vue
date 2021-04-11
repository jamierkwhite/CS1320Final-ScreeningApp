<template>
    <Page class="page">
        <ActionBar title="Full Echo">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <ScrollView>
            <StackLayout>
                <RadDataForm :source="patient" :metadata="patientMetadata"
                    @propertyCommitted="onPropertyCommitted" />
                <Button text="Submit" @tap="onButtonTap" class="regsubmit" />
            </StackLayout>
        </ScrollView>
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
                    anterior_mitral_valve_leaflet_thickness: "Normal",
                    posterior_mitral_valve_leaflet_thickness: "Normal",
                    posterior_mitral_valve_mobility: "Normal",
                    aortic_valve_thickness: "Normal",
                    mitral_valve_function: "Normal",
                    anterior_mitral_valve_mobility: "Normal",
                    mitral_regurgitation: "> 1.5cm",
                    aortic_valve_function: "Normal",
                    aortic_regurgitation: "> 1.5cm"
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
                            name: "anterior_mitral_valve_leaflet_thickness",
                            displayName: "Anterior Mitral Valve Leaflet Thickness",
                            index: 2,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "posterior_mitral_valve_leaflet_thickness",
                            displayName: "Posterior Mitral Valve Leaflet Thickness",
                            index: 3,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "posterior_mitral_valve_mobility",
                            displayName: "Posterior Mitral Valve Mobility",
                            index: 4,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "aortic_valve_thickness",
                            displayName: "Aortic Valve Thickness",
                            index: 5,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "mitral_valve_function",
                            displayName: "Mitral Valve Function",
                            index: 6,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "anterior_mitral_valve_mobility",
                            displayName: "Anterior Mitral Valve Mobility",
                            index: 7,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "mitral_regurgitation",
                            displayName: "Mitral Regurgitation",
                            index: 8,
                            editor: "SegmentedEditor",
                            valuesProvider: ["> 1.5cm", "< 1.5cm"]
                        },
                        {
                            name: "aortic_valve_function",
                            displayName: "Aortic Valve Function",
                            index: 9,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "aortic_regurgitation",
                            displayName: "Aortic Regurgitation",
                            index: 10,
                            editor: "SegmentedEditor",
                            valuesProvider: ["> 1.5cm", "< 1.5cm "]
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