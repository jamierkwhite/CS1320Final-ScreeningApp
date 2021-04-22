<template>
    <Page class="page">
        <!-- Page to show coming soon -->
        <StackLayout class="profile-page">
            <Label text="Coming Soon!" class="soon-label" />
        </StackLayout>
    </Page>
</template>

<script>
    export default {
        data() {
            return {};
        }
    };
</script>

<style scoped>
    .profile-page {
        vertical-align: center;
    }

    .soon-label {
        margin-bottom: 100;
        text-align: center;
        font-size: 30;
        font-weight: bold;
        text-decoration: underline;
        color: darkgray;
    }
</style>