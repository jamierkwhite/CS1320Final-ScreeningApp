<template>
    <Page class="page">
        <StackLayout class="form">
            <Image class="logo" src="~/images/logo2.png" />
            <Label class="header" text="RHDScreen"></Label>
            <StackLayout class="input-field">
                <TextField ref="username" class="input" hint="Username"
                    keyboardType="email" autocorrect="false"
                    autocapitalizationType="none" v-model="user.username"
                    returnKeyType="next" @returnPress="focusPassword()">
                </TextField>
                <StackLayout class="hr-light"></StackLayout>
            </StackLayout>
            <StackLayout class="input-field">
                <TextField ref="password" id="password" class="input"
                    hint="Password" secure="true" v-model="user.password"
                    returnKeyType="next"></TextField>
                <StackLayout class="hr-light"></StackLayout>
            </StackLayout>
            <StackLayout class="input-field">
                <TextField ref="confirmpassword" id="confirmpassword"
                    class="input" hint="Confirm Password" secure="true"
                    v-model="user.confirmpassword" returnKeyType="next">
                </TextField>
                <StackLayout class="hr-light"></StackLayout>
            </StackLayout>
            <StackLayout class="input-field">
                <TextField ref="registrationCode" id="registrationCode"
                    class="input" hint="Registration Code"
                    autocorrect="false" autocapitalizationType="none"
                    v-model="user.registrationCode" returnKeyType="done">
                </TextField>
                <StackLayout class="hr-light"></StackLayout>
            </StackLayout>
            <Button text="Register" @tap="submit()"
                class="btn btn-primary m-t-20" style="color: white"></Button>
            <Label @tap="toggleForm()" class="sign-up-group">
                <FormattedString>
                    <Span text="Back to Login" class="sign-up-label-bold">
                    </Span>
                    <Span text="" class="sign-up-label-bold">
                    </Span>
                </FormattedString>
            </Label>
        </StackLayout>


    </Page>
</template>
<script>
    import Login from "./Login";
    import {
        isIOS
    } from "tns-core-modules/platform";
    import {
        topmost
    } from "ui/frame";
    export default {
        name: "Login",
        data() {
            return {
                user: {
                    username: null,
                    password: null,
                    confirmpassword: null,
                    registrationCode: null
                },
                isLoggingIn: true
            };
        },
        methods: {
            submit() {
                if (!this.user.username || !this.user.password) {
                    this.alert(
                    "Please provide both a username and password.");
                    return;
                }
                if (this.user.password !== this.user.confirmpassword) {
                    this.alert("Passwords do not match.");
                    return;
                }
                if (this.user.registrationCode !== "Rc9ZEw") {
                    this.alert("Invalid Registration Code");
                    return;
                }
                this.login();
            },
            login() {
                this.$navigateTo(Login);
            },
            focusPassword() {
                this.$refs.password.nativeView.focus();
            },
            alert(message) {
                return alert({
                    title: "RHDScreen",
                    okButtonText: "OK",
                    message: message
                });
            },
            toggleForm() {
                this.isLoggingIn = !this.isLoggingIn;
                this.$navigateTo(Login);
            }
        }
    };
</script>

<style>
    .page {
        align-items: center;
        flex-direction: column;
    }

    .form {
        margin-left: 30;
        margin-right: 30;
        flex-grow: 2;
        vertical-align: middle;
    }

    .logo {
        margin-bottom: 12;
        height: 120;
        font-weight: bold;
    }

    .header {
        horizontal-align: center;
        font-size: 25;
        font-weight: 600;
        margin-bottom: 70;
        text-align: center;
        color: #D51A1A;
    }

    .input-field {
        margin-bottom: 25;
    }

    .input {
        font-size: 18;
        placeholder-color: #A8A8A8;
    }

    .btn-primary {
        height: 50;
        margin: 30 5 15 5;
        background-color: #D51A1A;
        border-radius: 5;
        font-size: 20;
        font-weight: 600;
    }

    .login-label {
        margin-top: 20;
        horizontal-align: center;
        color: #A8A8A8;
        font-size: 16;
    }

    .sign-up-group {
        margin-top: 50;
        horizontal-align: center;
        color: #A8A8A8;
        font-size: 16;
    }

    .sign-up-label {
        color: #A8A8A8;
        font-size: 16;
    }

    .sign-up-label-bold {
        font-weight: bold;
        color: #808080;
        font-size: 16;
    }

</style>