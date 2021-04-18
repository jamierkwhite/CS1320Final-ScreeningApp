<template>
    <Page class="page">
        <ActionBar title="Patient Search">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <ScrollView>
            <StackLayout>
                <FlexboxLayout flexDirection="row">
                    <SearchBar hint=" search patient id..."
                        :text="searchPhrase" textFieldHintColor="#BBBBBB"
                        @textChange="onSearchChange" @submit="onSearchSubmit"
                        class="mySearchBar"
                        style="font-size: 14pt; width: 85%;"
                        id="mySearchBar" />
                    <Button text="Cancel" @tap="onButtonTap"
                        class="button2" />
                </FlexboxLayout>
                <Label text="Patient List:"
                    style="font-size: 18px; margin-top: 50px; margin-bottom: 20px; margin-left: 20px; font-weight: bold;" />
                <ListView for="pat in patients" @itemTap="onItemTap"
                    style="height:1200px; border-width: 0.5; border-color: gray; margin-bottom:30px">
                    <v-template>
                        <FlexboxLayout flexDirection="column"
                            style="margin-top:15px; margin-bottom:15px">
                            <FlexboxLayout flexDirection="row" class="t-12">
                                <Label text="Name:"
                                    style="margin-right: 12px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.firstname"
                                    style="margin-right: 8px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.lastname"
                                    style="margin: 0px; padding: 0px; font-size: 14px" />
                            </FlexboxLayout>
                            <FlexboxLayout flexDirection="row" class="t-12"
                                style="margin-left: 10px; margin-top: 10x">
                                <Label text="Patient ID:"
                                    style="margin-right: 12px; padding: 0px; font-size: 14px" />
                                <Label :text="pat.patientid"
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
                                <Label :text="pat.consent"
                                    style="margin-right: 8px; padding: 0px; font-size: 14px; font-weight:bold"
                                    :class="pat.consent" />
                            </FlexboxLayout>
                            <!-- <Label :text="pat.patientid" class="t-12"
                                style="width: 60%" /> -->
                        </FlexboxLayout>
                    </v-template>
                </ListView>
            </StackLayout>
        </ScrollView>
    </Page>
</template>

<script>
    import ScreenWPatient from "./ScreenWPatient";
    var view = require("ui/core/view");
    import * as utils from "tns-core-modules/utils/utils";
    import {
        isIOS,
        isAndroid
    } from "tns-core-modules/platform";
    const http = require("tns-core-modules/http");
    export default {
        data() {
            return {
                patients: [{
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

                searching: ""
            };
        },

        // beforeMount() {
        //     this.getMyRestaurants();
        // },

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

            onItemTap: function(args) {
                console.log("Item with index: " + args.index + " tapped");
                console.log("Patient: " + this.patients[args.index]
                    .firstname);
                this.$navigateTo(ScreenWPatient, {
                    props: {
                        firstname: this.patients[args.index]
                            .firstname,
                        lastname: this.patients[args.index]
                            .lastname,
                        patientid: this.patients[args.index]
                            .patientid
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
            }

            // parseResponse(response) {
            //     this.restaurantss = [];
            //     console.log("parsing response");
            //     const results = response.content.toJSON().results;
            //     console.log(results.length);
            //     results.forEach(element => {
            //         console.log(element.name.replace("'", ""));
            //         const name = "Restuarant Name: " + element.name;
            //         const vicinity = "Vicinity: " + element.vicinity;
            //         var rating = "";
            //         if (typeof element.rating !== "number") {
            //             rating = "Rating: N/A";
            //         } else {
            //             rating = "Rating: " + element.rating;
            //         }
            //         const restInfo = {
            //             name: name,
            //             onlyName: element.name,
            //             vicinity: vicinity,
            //             rating: rating
            //         };
            //         this.restaurantss.push(restInfo);
            //     });
            //     this.restaurantss = this.restaurantss.slice(0, 10);
            //     this.ogrestaurantss = this.restaurantss;
            // },

            // getMyRestaurants() {
            //     geoLocation.enableLocationRequest();
            //     geoLocation
            //         .getCurrentLocation({
            //             desiredAccuracy: 100,
            //             updateDistance: 0.1,
            //             timeout: 20000
            //         })
            //         .then(
            //             loc => {
            //                 if (loc) {
            //                     console.log(loc);
            //                     const latitude = loc.latitude;
            //                     const longitude = loc.longitude;
            //                     const key =
            //                         "AIzaSyAidoOjLx4TvKFi8CEZzSc4hmR_y4PaAmI";
            //                     const request = "nearbysearch";
            //                     const output = "json";
            //                     const radius = 500;
            //                     const type = "restaurant";
            //                     const parameters =
            //                         "location=" + latitude + "," + longitude;
            //                     // const url =
            //                     //     `https://maps.googleapis.com/maps/api/place/${request}/${output}?${parameters}&radius=${radius}&type=${type}&key=${key}`;
            //                     const url =
            //                         `https://maps.googleapis.com/maps/api/place/${request}/${output}?${parameters}&rankby=distance&type=${type}&key=${key}`;
            //                     console.log(url);
            //                     http.request({
            //                         url: url,
            //                         method: "GET"
            //                     }).then(this.parseResponse);
            //                 }
            //             },
            //             function(e) {
            //                 console.log("Error: " + e.message);
            //             }
            //         );
            // }
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