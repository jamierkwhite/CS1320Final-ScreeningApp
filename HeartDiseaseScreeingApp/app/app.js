import Vue from 'nativescript-vue';

import Login from './components/Login';

// Uncommment the following to see NativeScript-Vue output logs
// Vue.config.silent = false;

new Vue({

    template: `
        <Frame>
            <Login />
        </Frame>`,

    components: {
        Login
    }
}).$start();