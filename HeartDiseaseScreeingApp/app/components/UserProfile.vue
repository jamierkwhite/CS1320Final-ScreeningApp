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
        </StackLayout>
    </Page>
</template>

<script>
    export default {
        data() {
            return {};
        },
        props: ["username"],
        methods: {
            onButtonTap() {
                console.log("Button was pressed");
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
</style>