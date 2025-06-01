<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';


const email = ref('');
const password = ref('');

console.log(email.value, password.value);

</script>

<template>
    <h1>Welcome to Grocery Store</h1>
    <h2>Login</h2>
    <form class = 'container-fluid'>
        <div class="mb-3">
            <label for="email">Email</label>
            <input type="text" v-model="email" id="email" required>
        </div>

        <p>{{ email }}</p>

        <div class = "mb-3">
            <label for="password">Password</label>
            <input type="password" v-model="password" id="password" required>
        </div>

        {{password}}
        <button type="submit">Login</button>
    </form>
    <RouterLink to='/register'>Create new User?</RouterLink>

</template>