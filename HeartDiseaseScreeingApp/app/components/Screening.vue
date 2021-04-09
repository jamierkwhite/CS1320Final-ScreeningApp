<template>
    <Page class="page">
        <ActionBar title="Registration">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <!-- <RadDataForm :source="album" /> -->
        <StackLayout>
            <RadDataForm :source="ticket" :metadata="ticketMetadata"
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
                album: {
                    bandName: "Ed Sheeran",
                    albumName: "X",
                    year: "2017",
                    owned: true,
                    myRating: "9.5"
                },
                ticket: {
                    movie: "Zootopia",
                    date: null,
                    time: null,
                    type: "2D",
                    price: 9,
                    numberOfTickets: 2
                },
                ticketMetadata: {
                    isReadOnly: false,
                    commitMode: "Immediate",
                    validationMode: "Immediate",
                    propertyAnnotations: [{
                            name: "movie",
                            displayName: "Movie Name",
                            index: 0,
                            editor: "Text"
                        },
                        {
                            name: "date",
                            displayName: "Date",
                            index: 1,
                            editor: "DatePicker"
                        },
                        {
                            name: "time",
                            displayName: "Time",
                            index: 2,
                            editor: "TimePicker"
                        },
                        {
                            name: "type",
                            displayName: "Type",
                            index: 3,
                            editor: "SegmentedEditor",
                            valuesProvider: ["2D", "3D"]
                        },
                        {
                            name: "price",
                            displayName: "Price",
                            index: 4,
                            editor: "Decimal",
                            readOnly: true
                        },
                        {
                            name: "numberOfTickets",
                            displayName: "Number Of Tickets",
                            index: 5,
                            editor: "Stepper",
                            editorParams: {
                                minimum: 0,
                                maximum: 20,
                                step: 2
                            }
                            // },
                            // {
                            //     name: "contactName",
                            //     displayName: "Contact Name",
                            //     index: 6,
                            //     editor: "Text"
                            // },
                            // {
                            //     name: "contactPhone",
                            //     displayName: "Contact Phone",
                            //     index: 7,
                            //     editor: "Phone"
                            // },
                            // {
                            //     name: "contactEmail",
                            //     displayName: "Contact Email",
                            //     index: 8,
                            //     editor: "Email"
                            // },
                            // {
                            //     name: "agreeTerms",
                            //     displayName: "I Agree with Terms",
                            //     index: 9,
                            //     editor: "Switch"
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

<style>
    DataFormEditorLabel {
        color: #212121;
        font-style: italic;
        font-weight: bold;
        font-size: 16;
    }

    .regsubmit {
        background-color: #24b39d;
        color: white;
        font-size: 16;
        font-weight: bold;
        width: 200;
        border-radius: 12px;
    }
</style>