<template>
    <Page @loaded="pageLoaded" class="page">
        <ActionBar title="Login">
            <NavigationButton visibility="collapsed" />
        </ActionBar>
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
                    returnKeyType="done"></TextField>
                <StackLayout class="hr-light"></StackLayout>
            </StackLayout>
            <Button text="Login" @tap="submit()"
                class="btn btn-primary m-t-20" style="color: white"></Button>
            <Label text="Forgot your password?" class="login-label"
                @tap="forgotPassword()"></Label>
            <Label @tap="toggleForm()" v-if="isLoggingIn"
                class="sign-up-group">
                <FormattedString>
                    <Span text="Don’t have an account? "
                        class="sign-up-label">
                    </Span>
                    <Span text="Sign up" class="sign-up-label-bold">
                    </Span>
                </FormattedString>
            </Label>
            <Label @tap="toggleForm()" v-if="!isLoggingIn"
                class="sign-up-group">
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
    import HelloWorld from "./HelloWorld";
    import UserRegistration from "./UserRegistration";
    import {
        Http,
        HttpResponse
    } from "@nativescript/core";
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
                    password: null
                },
                isLoggingIn: true
            };
        },
        created() {},
        methods: {
            pageLoaded() {
                //PAGE LOADED
            },
            submit() {
                if (!this.user.username || !this.user.password) {
                    this.alert(
                    "Please provide both a username and password.");
                    return;
                }
                this.login();
            },
            login() {
                // ADD YOUR OWN CODE
                // this.$navigateTo(HelloWorld, {
                //     props: {
                //         username: this.user.username
                //     }
                // });

                // EXAMPLE POST REQUEST TO LOGIN
                Http.request({
                    url: "https://rhd-screening.herokuapp.com/login",
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    content: JSON.stringify({
                        username: this.user.username,
                        password: this.user.password
                    })
                }).then(response => {
                        const result = response.content.toJSON();
                        console.log(`Http POST Result: ${result}`);
                        this.$navigateTo(HelloWorld, {
                            props: {
                                username: this.user.username,
                                token: result.token
                            }
                        });
                    },
                    e => {
                        console.log(e);
                        this.alert("Invalid username and/or password.");
                    }
                );
            },
            //     then((response: HttpResponse) => {
            //         const result = response.content.toJSON();
            //         console.log(`Http POST Result: ${result}`);
            //         this.$navigateTo(HelloWorld, {
            //             props: {
            //                 username: this.user.username,
            //                 token: result.token
            //             }
            //         });
            //     }, e => {
            //         console.log(e);
            //         this.alert("Invalid username and/or password.");
            //     });
            // },
            forgotPassword() {
                prompt({
                    title: "Forgot Password",
                    message: "Enter the email address you used to register for this app to reset your password.",
                    inputType: "email",
                    defaultText: "",
                    okButtonText: "Ok",
                    cancelButtonText: "Cancel"
                }).then(data => {
                    if (data.result) {
                        // ADD YOUR OWN CODE
                    }
                });
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
                this.$navigateTo(UserRegistration);
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

    .bold {
        color: #000000;
    }
</style>
