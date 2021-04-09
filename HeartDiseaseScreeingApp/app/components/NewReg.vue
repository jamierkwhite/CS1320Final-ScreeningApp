<template>
    <Page class="page">
        <ActionBar title="Registration">
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
                    first_name: "",
                    last_name: "",
                    dob: null,
                    age: null,
                    school: "",
                    standard: null,
                    village: "",
                    sub_county: "",
                    church: "",
                    home: "",
                    care_taker: "",
                    father: "",
                    mother: "",
                    phone1: null,
                    phone2: null
                },
                patientMetadata: {
                    isReadOnly: false,
                    commitMode: "Immediate",
                    validationMode: "Immediate",
                    propertyAnnotations: [{
                            name: "first_name",
                            displayName: "First Name",
                            index: 0,
                            editor: "Text"
                        },
                        {
                            name: "last_name",
                            displayName: "Last Name",
                            index: 1,
                            editor: "Text"
                        },
                        {
                            name: "dob",
                            displayName: "Date of Birth",
                            index: 2,
                            editor: "DatePicker"
                        },
                        {
                            name: "age",
                            displayName: "Age",
                            index: 3,
                            editor: "Number"
                        },
                        {
                            name: "school",
                            displayName: "School",
                            index: 4,
                            editor: "Text"
                        },
                        {
                            name: "standard",
                            displayName: "Standard",
                            index: 5,
                            editor: "Number"
                        },
                        {
                            name: "village",
                            displayName: "Village",
                            index: 6,
                            editor: "Text"
                        },
                        {
                            name: "sub_county",
                            displayName: "Sub-County",
                            index: 7,
                            editor: "Text"
                        },
                        {
                            name: "church",
                            displayName: "Church",
                            index: 8,
                            editor: "Text"
                        },
                        {
                            name: "home",
                            displayName: "Home Location",
                            index: 9,
                            editor: "Text"
                        },
                        {
                            name: "care_taker",
                            displayName: "Care Taker",
                            index: 10,
                            editor: "Text"
                        },
                        {
                            name: "father",
                            displayName: "Father",
                            index: 11,
                            editor: "Text"
                        },
                        {
                            name: "mother",
                            displayName: "Mother",
                            index: 12,
                            editor: "Text"
                        },
                        {
                            name: "phone1",
                            displayName: "Primary Phone",
                            index: 13,
                            editor: "Phone"
                        },
                        {
                            name: "phone2",
                            displayName: "Alternate Phone",
                            index: 14,
                            editor: "Phone"
                        }
                    ]
                },
                committedPerson: {}
            };
        },
        methods: {
            onButtonTap() {
                console.log(this.committedPerson);
            },
            onPropertyCommitted(data) {
                this.committedPerson = data.object.editedObject;
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
    }

    DataFormEditorCore {
        margin: 5;
        padding: 5;
        border-color: darkgray;
        border-width: 2;
        border-radius: 5;
        font-size: 14;
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