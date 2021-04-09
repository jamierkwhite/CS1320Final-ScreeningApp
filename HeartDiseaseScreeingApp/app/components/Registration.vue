<template>
    <Page class="page">
        <ActionBar title="Registration">
            <ActionItem @tap="onButtonTap" icon="res://home"
                ios.position="right" android.position="actionBar">
            </ActionItem>
            <!-- <NavigationButton visibility="collapsed" /> -->
        </ActionBar>
        <Label text="hello world!" />
    </Page>
</template>

<script>
    export default {
        data() {
            return {};
        }
    };
</script>

<style>
</style>