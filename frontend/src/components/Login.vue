<script setup>
import { pushScopeId } from 'vue';
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

import {useRouter} from 'vue-router'

const router = useRouter();


let isvacant = ref(false);
function changeVacancy(){
    isvacant.value = !isvacant.value;
}




const email = ref('');
const password = ref('');


const counter = ref(0);
function incrementCounter() {
    return counter.value++;
};


function checkPassword(){
    if (password.value.length < 6) {
        // alert('Password must be at least 6 characters long');
        return false;
    }
    return true;
}

async function login(){
    if (!checkPassword()){
        alert('Password must be at least 6 characters long');
        return;
    }
    const data = await fetch('http://localhost:5000/api/auth/login', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email.value,
            password: password.value
        })
    })
    if (!data.ok){
        const result = await data.json();
        console.log(result);
    }
    else {
        const result = await data.json();
        console.log(result);

        alert(result.message);
        localStorage.setItem('token', result.auth_token);

        router.push('/');
    }

    console.log(data);
}


console.log(email.value, password.value);

</script>

<template>
    <button @click="incrementCounter">Click me</button>
    <p>Counter: {{ counter }}</p>


    <button @click="changeVacancy" :class="{'btn btn-primary':isvacant}">Change Vacancy</button>

    <h1>Welcome to Grocery Store</h1>
    <h2>Login</h2>
    <form class = 'container-fluid' @submit.prevent = "login">
        <div class="mb-3">
            <label for="email">Email</label>
            <input type="text" v-model="email" id="email" required>
        </div>
        <div class = "mb-3">
            <label for="password">Password</label>
            <input type="password" v-model="password" id="password" required>
        </div>


        <p v-if="!checkPassword()">Password must be 6 digit long</p>


        <button type="submit">Login</button>
    </form>

    

    <RouterLink to='/register'>Create new User?</RouterLink>

</template>