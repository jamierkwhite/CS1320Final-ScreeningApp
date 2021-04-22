<template>
    <Page class="page">
        <ActionBar title="Screening">
            <ActionItem @tap="goHome" icon="res://home" ios.position="right"
                android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <ScrollView>
            <StackLayout>
                <!-- Diplay patient information -->
                <FlexboxLayout flexDirection="column"
                    style="margin-top:30px; margin-bottom: 40px; padding-bottom: 30px; border-color: black; border-width: 0 0 2 0; width:95%"
                    alignItems="center" justifyContent="center"
                    alignContent="center">
                    <FlexboxLayout flexDirection="row" class="t-12"
                        alignItems="center" justifyContent="center"
                        alignContent="center">
                        <Label text="Name:"
                            style="margin-right: 12px; padding: 0px; font-size: 18px; font-weight: bold" />
                        <Label :text="this.firstname"
                            style="margin-right: 8px; padding: 0px; font-size: 18px; font-weight: bold" />
                        <Label :text="this.lastname"
                            style="margin: 0px; padding: 0px; font-size: 18px; font-weight: bold" />
                    </FlexboxLayout>
                    <FlexboxLayout flexDirection="row" class="t-12"
                        style="margin-top: 10x" alignItems="center"
                        justifyContent="center" alignContent="center">
                        <Label text="Patient ID:"
                            style="margin-right: 12px; padding: 0px; font-size: 18px; font-weight: bold" />
                        <Label :text="this.patientid"
                            style="margin-right: 8px; padding: 0px; font-size: 18px; font-weight: bold" />
                    </FlexboxLayout>
                </FlexboxLayout>
                <!-- Basic Screening form -->
                <RadDataForm :source="patient" :metadata="patientMetadata"
                    @propertyCommitted="onPropertyCommitted" />
                <Button text="Submit" @tap="onButtonTap" class="regsubmit" />
            </StackLayout>
        </ScrollView>
    </Page>
</template>

<script>
    import HelloWorld from "./HelloWorld";
    import Vue from "nativescript-vue";
    import RadDataForm from "nativescript-ui-dataform/vue";
    Vue.use(RadDataForm);
    import {
        Http,
        HttpResponse
    } from "@nativescript/core";
    const userntoken = require("./UserTokenMap.js");

    export default {
        data() {
            return {
                patient: {
                    date: "",
                    location: "",
                    am_valve_leaflet_thickness_normality: "Normal",
                    pm_valve_leaflet_thickness_normality: "Normal",
                    am_valve_mobility_normality: "Normal",
                    pm_valve_mobility_normality: "Normal",
                    a_valve_thickness_normality: "Normal",
                    a_valve_function_normality: "Normal",
                    m_valve_function_normality: "Normal"
                },
                patientMetadata: {
                    isReadOnly: false,
                    commitMode: "Immediate",
                    validationMode: "Immediate",
                    propertyAnnotations: [{
                            name: "date",
                            displayName: "Date",
                            index: 0,
                            editor: "Text"
                        },
                        {
                            name: "location",
                            displayName: "Location",
                            index: 1,
                            editor: "Text"
                        },
                        {
                            name: "am_valve_leaflet_thickness_normality",
                            displayName: "Anterior Mitral Valve Leaflet Thickness",
                            index: 2,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "pm_valve_leaflet_thickness_normality",
                            displayName: "Posterior Mitral Valve Leaflet Thickness",
                            index: 3,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "am_valve_mobility_normality",
                            displayName: "Anterior Mitral Valve Mobility",
                            index: 4,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "pm_valve_mobility_normality",
                            displayName: "Posterior Mitral Valve Mobility",
                            index: 5,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "a_valve_thickness_normality",
                            displayName: "Aortic Valve Thickness",
                            index: 6,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "a_valve_function_normality",
                            displayName: "Aortic Valve Function",
                            index: 7,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        },
                        {
                            name: "m_valve_function_normality",
                            displayName: "Mitral Valve Function",
                            index: 8,
                            editor: "SegmentedEditor",
                            valuesProvider: ["Normal", "Abnormal"]
                        }
                    ]
                },
                committedPerson: {},
                today_date: " ",
                datetimeobj: null,
                username: userntoken[0].username,
                token: userntoken[0].token
            };
        },
        props: ["firstname", "lastname", "patientid"],
        beforeMount() {
            this.getDate();
            this.committedPerson = JSON.stringify(this.patient);
        },
        methods: {
            // Submits basic screening form and redirects user home
            onButtonTap() {
                console.log("Button tapped");
                this.committedPerson = JSON.parse(this.committedPerson);
                console.log(this.committedPerson);
                this.committedPerson.date = this.datetimeobj;
                this.committedPerson.id = this.patientid;
                this.committedPerson["aortic_regurgitation"] = "n/a";
                this.committedPerson["mitral_regurgitation"] = "n/a";
                this.committedPerson["comments"] = "n/a";
                console.log(this.committedPerson);
                this.committedPerson = JSON.stringify(this.committedPerson);
                console.log(this.committedPerson);

                // EXAMPLE POST REQUEST TO SUMBIT BASIC SCREENING
                Http.request({
                    url: "https://rhd-screening.herokuapp.com/screening_echo",
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    content: JSON.stringify({
                        token: this.token,
                        patient_info: this.committedPerson
                    })
                }).then(
                    response => {
                        let self = this;
                        alert({
                            title: "RHDScreen",
                            okButtonText: "go home",
                            message: "Basic Screen Submitted Successfully!"
                        }).then(function() {
                            console.log("going home");
                            self.goHome();
                        });
                    },
                    function(e) {
                        console.log("Error:" + e.message);
                        alert({
                            title: "RHDScreen ",
                            okButtonText: "OK ",
                            message: "Error. Try Again."
                        });
                    }
                );
            },
            // Redirects user home
            goHome() {
                console.log("really going home");
                this.$navigateTo(HelloWorld, {
                    props: {
                        username: this.username,
                        token: this.token
                    }
                });
            },
            // Committs data when form field editted
            onPropertyCommitted(data) {
                console.log(data.object.editedObject);
                this.committedPerson = data.object.editedObject;
            },
            // Gets today's date
            getDate() {
                var today = new Date();
                this.datetimeobj = today;
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
        margin: 15;
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