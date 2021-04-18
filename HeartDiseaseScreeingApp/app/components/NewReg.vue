<template>
    <Page class="page">
        <ActionBar title="Registration">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <!-- <RadDataForm :source="album" /> -->
        <ScrollView>
            <StackLayout>
                <GridLayout columns="*, *" rows="*" height="100"
                    style="margin-bottom: 40px">
                    <FlexboxLayout row="0" col="0" flexDirection="column"
                        @tap="takeRegPhoto()" backgroundColor="transparent"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-right: 20px; margin-top: 20px">
                        <Image src="~/images/camera.png" height="75"
                            width="75" style="margin-top: 6px;" />
                        <Label text="Add Patient Picture" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                    <FlexboxLayout row="0" col="1" flexDirection="column"
                        @tap="takeRegPhoto()" backgroundColor="transparent"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-right: 20px; margin-top: 20px">
                        <Image src="~/images/add_doc.png" height="75"
                            width="75" style="margin-top: 6px;" />
                        <Label text="Add Consent Forms" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                </GridLayout>
                <RadDataForm :source="patient" :metadata="patientMetadata"
                    @propertyCommitted="onPropertyCommitted"
                    style="margin-bottom:40px" />
                <Button text="Submit" @tap="onButtonTap" class="regsubmit" />
            </StackLayout>
        </ScrollView>
    </Page>
</template>

<script>
    import Vue from "nativescript-vue";
    import RadDataForm from "nativescript-ui-dataform/vue";
    Vue.use(RadDataForm);
    var camera = require("nativescript-camera");
    var imageModule = require("tns-core-modules/ui/image");
    import {
        Http,
        HttpResponse
    } from "@nativescript/core";

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
        props: ["token"],
        methods: {
            onButtonTap() {
                // LOGS THE PATIENT REGISTRATION DATA THAT HAS BEEN INPUTTED
                console.log(this.committedPerson);

                // EXAMPLE POST REQUEST TO REGISTER PATIENT
                Http.request({
                        url: "https://rhd-screening.herokuapp.com/register",
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        content: JSON.stringify({
                            token: this.token,
                            patientinfo: this.committedPerson
                        })
                    }).then(response => {
                        const result = response.content.toJSON();
                        console.log(`Http POST Result: ${result}`);
                        this.$navigateTo(HelloWorld, {
                            props: {
                                token: this.token
                            }
                        });
                    },
                    function(e) {
                        console.log("Error: " + e.message);
                        this.alert("Error: " + e.message); //e.statusCode
                    });
            },
            //     then((response: HttpResponse) => {
            //         const result = response.content.toJSON();
            //         console.log(`Http POST Result: ${result}`);
            //         this.$navigateTo(HelloWorld, {
            //             props: {
            //                 token: this.token
            //             }
            //         });
            //     }, e => {
            //         console.log(e);
            //         this.alert(e);
            //     });
            // },
            onPropertyCommitted(data) {
                this.committedPerson = data.object.editedObject;
            },
            takeRegPhoto() {
                camera
                    .takePicture()
                    .then(function(imageAsset) {
                        console.log("Result is an image asset instance");
                        var image = new imageModule.Image();
                        image.src = imageAsset;
                    })
                    .catch(function(err) {
                        console.log("Error -> " + err.message);
                    });
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
