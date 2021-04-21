<template>
    <Page class="page">
        <ActionBar title="Patient Search">
            <ActionItem @tap="onButtonTap2" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <ScrollView>
            <StackLayout>
                <FlexboxLayout flexDirection="row">
                    <SearchBar hint=" search patient id..."
                        :text="searchPhrase" textFieldHintColor="#BBBBBB"
                        @submit="getPatients" class="mySearchBar"
                        style="font-size: 14pt; width: 85%;"
                        id="mySearchBar" />
                    <Button text="Cancel" @tap="onButtonTap"
                        class="button2" />
                </FlexboxLayout>
                <FlexboxLayout flexDirection="row-reverse">
                    <Button :text="this.currentFilter" @tap="onFilterTap()"
                        class="button3" />
                </FlexboxLayout>
                <Label text="Patient List:"
                    style="font-size: 18px; margin-top: 50px; margin-bottom: 20px; margin-left: 20px; font-weight: bold;" />
                <ListView ref="listView" for="pat in patients"
                    @itemTap="onItemTap"
                    style="height:1200px; border-width: 0.5; border-color: gray; margin-bottom:30px">
                    <v-template>
                        <FlexboxLayout flexDirection="column"
                            style="margin-top:15px; margin-bottom:15px">
                            <FlexboxLayout flexDirection="row" class="t-12">
                                <Label text="Name:"
                                    style="margin-right: 12px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.first_name"
                                    style="margin-right: 8px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.last_name"
                                    style="margin: 0px; padding: 0px; font-size: 14px" />
                            </FlexboxLayout>
                            <FlexboxLayout flexDirection="row" class="t-12"
                                style="margin-left: 10px; margin-top: 10x">
                                <Label text="Patient ID:"
                                    style="margin-right: 12px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.id"
                                    style="margin-right: 8px; padding: 0px; font-size: 14px" />
                            </FlexboxLayout>
                            <FlexboxLayout flexDirection="row" class="t-12"
                                style="margin-left: 10px; margin-top: 10x">
                                <Label text="Age:"
                                    style="margin-right: 12px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.age"
                                    style="margin-right: 8px; padding: 0px; font-size: 14px" />
                            </FlexboxLayout>
                            <FlexboxLayout flexDirection="row" class="t-12"
                                style="margin-left: 10px; margin-top: 10x">
                                <Label text="Screening Consent:"
                                    style="margin-right: 12px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.consent_url"
                                    style="margin-right: 8px; padding: 0px; font-size: 14px; font-weight:bold"
                                    :class="pat.consent_url" />
                            </FlexboxLayout>>
                        </FlexboxLayout>
                    </v-template>
                </ListView>
            </StackLayout>
        </ScrollView>
    </Page>
</template>

<script>
    import HelloWorld from "./HelloWorld";
    import ScreenWPatient from "./ScreenWPatient2";
    var view = require("ui/core/view");
    import * as utils from "tns-core-modules/utils/utils";
    import {
        isIOS,
        isAndroid
    } from "tns-core-modules/platform";
    import {
        Http,
        HttpResponse
    } from "@nativescript/core";
    const userntoken = require("./UserTokenMap.js");
    export default {
        data() {
            return {
                patients: [],

                allPatients: [{
                        firstname: "Evans",
                        lastname: "Kipkoech",
                        patientid: "13A4E",
                        age: 12,
                        consent: "Yes"
                    },
                    {
                        firstname: "Elvis",
                        lastname: "Kipkoech",
                        patientid: "22F2A",
                        age: 15,
                        consent: "Yes"
                    },
                    {
                        firstname: "Enoch",
                        lastname: "Kipkoech",
                        patientid: "26DEA",
                        age: 7,
                        consent: "No"
                    }
                ],

                searchPhrase: "",

                searching: "",

                currentFilter: "id",

                username: userntoken[0].username,

                token: userntoken[0].token
            };
        },
        // props: ["username", "token"],

        methods: {
            onButtonTap() {
                console.log("Button was pressed");
                if (isIOS) {
                    UIApplication.sharedApplication.keyWindow.endEditing(
                    true);
                }
                if (isAndroid) {
                    utils.ad.dismissSoftInput();
                }
            },

            onButtonTap2() {
                console.log("Button was pressed");
                console.log(this.username);
                console.log(this.token);
                this.$navigateTo(HelloWorld, {
                    props: {
                        username: this.username,
                        token: this.token
                    }
                });
            },

            onFilterTap() {
                action("Choose Filter", "Cancel", [
                    "id",
                    "first_name",
                    "last_name"
                ]).then(result => {
                    if (result == "Cancel") {
                        this.currentFilter = this.currentFilter;
                    } else {
                        this.currentFilter = result;
                    }
                });
            },

            onItemTap: function(args) {
                console.log("Item with index: " + args.index + " tapped");
                console.log("Patient: " + this.patients[args.index]
                    .firstname);
                this.$navigateTo(ScreenWPatient, {
                    props: {
                        firstname: this.patients[args.index]
                            .first_name,
                        lastname: this.patients[args.index]
                            .last_name,
                        patientid: this.patients[args.index].id
                    }
                });
            },

            onClear(args) {
                console.log("clearing");
                var search = args.object;
                setTimeout(() => {
                    search.dismissSoftInput();
                }, 0);
            },

            onSearchSubmit(args) {
                let searchBar = args.object;
                console.log("You are searching for " + searchBar.text);
            },

            onSearchChange(args) {
                let searchBar = args.object;
                var searchText = searchBar.text;
                if (searchText == null) {
                    searchText = "";
                }
                console.log("You are searching for " + searchText);
                this.searching = searchText;
                const filteredResult = this.allPatients.filter(pat =>
                    pat.patientid.toLowerCase().includes(searchText
                        .toLowerCase())
                );
                this.patients = filteredResult;
            },

            getPatients(args) {
                this.patients = [];
                let searchBar = args.object;
                var searchText = searchBar.text;
                if (searchText == null) {
                    searchText = "";
                }
                console.log("You searching for " + searchText);
                this.searching = searchText;
                const searchFor = this.currentFilter;
                var postreqcontent = null;
                if (searchFor == "id") {
                    postreqcontent = JSON.stringify({
                        id: this.searching
                    });
                }
                if (searchFor == "first_name") {
                    postreqcontent = JSON.stringify({
                        first_name: this.searching
                    });
                }
                if (searchFor == "last_name") {
                    postreqcontent = JSON.stringify({
                        last_name: this.searching
                    });
                }
                console.log(searchFor);
                Http.request({
                    url: "https://rhd-screening.herokuapp.com/find_patients",
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    content: postreqcontent
                }).then(
                    response => {
                        console.log(response);
                        console.log(response.content.toString());
                        const result = response.content.toJSON();
                        console.log(result);
                        console.log(`Http POST Result:${result}`);
                        console.log(typeof result);
                        result.forEach(element => {
                            console.log("here");
                            if (element.consent_url === null) {
                                element.consent_url = "No";
                            } else {
                                element.consent_url = "Yes";
                            }
                        });
                        this.patients = result;
                        this.$refs.listView.nativeView.refresh();
                    },
                    function(e) {
                        console.log("Error: " + e.message);
                        this.alert("Error: " + e.message); //e.statusCode
                    }
                );
            }
        }
    };
</script>

<style>
    .search-bar {
        border-width: 0.5;
        border-color: gray;
    }

    .icon {
        margin-left: 15px;
    }

    .button2 {
        background-color: #999999;
        color: white;
        padding: 0rem;
        margin: 0px;
    }

    .button3 {
        background-color: #D51A1A;
        color: white;
        padding: 1rem;
        margin-right: 10px;
        margin-top: 20px;
        border-radius: 80;
        width: 250px;
    }

    .mySearchBar {
        padding-bottom: 40px;
    }

    .Yes {
        color: green;
    }

    .No {
        color: red;
    }
</style>