import Vue from 'nativescript-vue';

import Login from './components/Login';

// Uncommment the following to see NativeScript-Vue output logs
// Vue.config.silent = false;

// Loads login page upon starting the app
new Vue({

    template: `
        <Frame>
            <Login />
        </Frame>`,

    components: {
        Login
    }
}).$start();

// new Vue({
//     render: (h) => h('frame', [h(Login)]),
//   }).$start()