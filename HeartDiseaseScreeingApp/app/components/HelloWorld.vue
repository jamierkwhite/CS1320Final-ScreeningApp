<template>
    <Page backgroundColor="#ffcfcc">
        <ActionBar title="Home">
            <NavigationButton visibility="collapsed" />
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="left" android.position="actionBar"></ActionItem>
            <ActionItem @tap="onTapProfile" icon="res://settings"
                ios.position="right" android.position="popup"></ActionItem>
            </ActionItem>
        </ActionBar>
        <ScrollView>
            <StackLayout class="home-panel">
                <!-- home screen content here-->
                <Image class="logo" src="~/images/logo_real.png" height="150"
                    style="margin-bottom: 75px" />
                <GridLayout columns="*, *" rows="*, *, *" height="500">
                    <FlexboxLayout row="0" col="0" flexDirection="column"
                        @tap="goTo('comesoon')" backgroundColor="#E4F2FD"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-right: 20px; margin-top: 20px">
                        <Image src="~/images/scheduling.jpg" height="125"
                            width="125" style="margin-top: 6px;" />
                        <Label text="Scheduling" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                    <FlexboxLayout row="0" col="1" flexDirection="column"
                        @tap="goTo('comesoon')" backgroundColor="#E4F2FD"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-left: 20px; margin-top: 20px">
                        <Image src="~/images/mileage.jpg" height="125"
                            width="125" style="margin-top: 6px;" />
                        <Label text="Mileage" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                    <FlexboxLayout row="1" col="0" flexDirection="column"
                        @tap="goTo('patsearchecho')" backgroundColor="#E4F2FD"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-right: 20px; margin-top: 20px">
                        <Image src="~/images/full_echo.jpg" height="125"
                            width="125" style="margin-top: 6px;" />
                        <Label text="Full Echo" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                    <FlexboxLayout row="1" col="1" flexDirection="column"
                        @tap="goTo('patsearchpcn')" backgroundColor="#E4F2FD"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-left: 20px; margin-top: 20px">
                        <Image src="~/images/penicillin.jpg" height="125"
                            width="125" style="margin-top: 6px;" />
                        <Label text="Penicillin" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                    <FlexboxLayout row="2" col="0" flexDirection="column"
                        @tap="goTo('patsearchscreen')"
                        backgroundColor="#E4F2FD" alignItems="center"
                        justifyContent="center" alignContent="center"
                        style="margin-right: 20px; margin-top: 20px">
                        <Image src="~/images/screening.jpg" height="125"
                            width="125" style="margin-top: 6px;" />
                        <Label text="Screening" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                    <FlexboxLayout row="2" col="1" flexDirection="column"
                        @tap="goTo('newreg')" backgroundColor="#E4F2FD"
                        alignItems="center" justifyContent="center"
                        alignContent="center"
                        style="margin-left: 20px; margin-top: 20px">
                        <Image src="~/images/registration.jpg" height="130"
                            width="130" />
                        <Label text="Registration" color="black"
                            style="font-weight: bold;" />
                    </FlexboxLayout>
                </GridLayout>
            </StackLayout>
        </ScrollView>
    </Page>
</template>

<script>
    import Registration from "./Registration";
    import NewReg from "./NewReg";
    import NewScren from "./NewScren";
    import AdvancedScreening from "./AdvancedScreening";
    import PenicillinScreen from "./PenicillinScreen";
    import UserProfile from "./UserProfile";
    import ComingSoon from "./ComingSoon";
    import PatientSearch from "./PatientSearch";
    import PatientSearchScreen from "./PatientSearchScreen2";
    import PatientSearchEcho from "./PatientSearchEcho";
    import PatientSearchPCN from "./PatientSearchPCN";
    const userntoken = require("./UserTokenMap.js");

    export default {
        data() {
            return {
                routes: {
                    reg: Registration,
                    newreg: NewReg,
                    newscreen: NewScren,
                    advscreen: AdvancedScreening,
                    pcnscreen: PenicillinScreen,
                    comesoon: ComingSoon,
                    patsearch: PatientSearch,
                    patsearchscreen: PatientSearchScreen,
                    patsearchecho: PatientSearchEcho,
                    patsearchpcn: PatientSearchPCN
                }
            };
        },
        props: ["username", "token"],
        methods: {
            onButtonTap() {
                console.log("Button was pressed");
                console.log(userntoken);
            },
            onTapProfile() {
                console.log(this.username);
                this.$navigateTo(UserProfile, {
                    props: {
                        username: this.username
                    }
                });
            },
            goTo(s) {
                console.log("going to page");
                if (s === "newreg") {
                    this.$navigateTo(this.routes["newreg"], {
                        props: {
                            token: this.token,
                            username: this.username
                        }
                    });
                } else {
                    this.$navigateTo(this.routes[s], {
                        props: {
                            username: this.username,
                            token: this.token
                        }
                    });
                }
            }
        }
    };
</script>

<style scoped>
    .home-panel {
        vertical-align: center;
        font-size: 20;
        margin: 15;
    }

    .description-label {
        margin-bottom: 15;
        text-align: center;
    }
</style>