// authMachine.js
import { createMachine } from 'xstate';

const authMachine = createMachine({
  id: 'auth',
  initial: 'loggedOut',
  states: {
    loggedOut: {
      on: {
        LOGIN: 'loggedIn'
      }
    },
    loggedIn: {
      on: {
        LOGOUT: 'loggedOut'
      }
    }
  }
});

export default authMachine;
