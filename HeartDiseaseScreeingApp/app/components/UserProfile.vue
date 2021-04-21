<template>
    <Page class="page">
        <ActionBar title="Profile">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
        </ActionBar>
        <StackLayout class="profile-page">
            <Label text="Welcome!" class="description-label-welcome" />
            <FlexboxLayout flexDirection="row" alignItems="center"
                justifyContent="center" alignContent="center">
                <Label text="username: " class="description-label-profile" />
                <Label :text="this.username"
                    class="description-label-profile" />
            </FlexboxLayout>
            <Label text="Check back later for more information"
                class="description-label-profile"
                style="color: darkgray; margin-top:100" />
            <Label text="Logout" class="logout" @tap="gotoLogin()"></Label>
        </StackLayout>
    </Page>
</template>

<script>
    import Login from "./Login";
    const userntoken = require("./UserTokenMap.js");
    export default {
        data() {
            return {
                username: userntoken[0].username,
                token: userntoken[0].token
            };
        },
        // props: ["username"],
        methods: {
            onButtonTap() {
                console.log("Button was pressed");
            },
            gotoLogin() {
                this.$navigateTo(Login);
            }
        }
    };
</script>

<style>
    .profile-page {
        vertical-align: center;
        margin: 15;
    }

    .description-label-welcome {
        margin-bottom: 25;
        text-align: center;
        font-size: 30;
        font-weight: bold;
        text-decoration: underline
    }

    .description-label-profile {
        margin-bottom: 15;
        text-align: center;
        font-size: 20;
    }

    .logout {
        margin-bottom: 15;
        margin-top: 50;
        color: gray;
        text-align: center;
        font-size: 20;
        font-weight: bold;
    }
</style>