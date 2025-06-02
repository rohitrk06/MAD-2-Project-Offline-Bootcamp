<script setup>
import { RouterLink } from 'vue-router'
import { onMounted, computed, ref } from 'vue';

onMounted(() => {
    isAuthenticated();
    get_currentUser();
});
let user_login = ref('false');

// const isAuthenticated = computed(()=>{
//     return localStorage.getItem('token') !== null;
// })

function isAuthenticated(){
    const token = localStorage.getItem('token');
    user_login.value = true
    console.log(user_login.value);
    return token !== null;
}

function get_currentUser() {
    const token = localStorage.getItem('token');
    if (!token){
      return null;
    }
    
    fetch('http://localhost:5000/api/get_current_user', {
        method: 'GET',
        headers:{
            'Content-Type': 'application/json',
            'Authentication-Token': token
        }
    })
    .then((response) =>{
          if (response.ok){
            return response.json();
          }
    })
    .then((data) => {
          console.log(data);
    })
 
}

function logout_user(){
    fetch('http://localhost:5000/api/auth/logout',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'Authentication-Token': localStorage.getItem('token')
        }
    }).then((response) => {
      if (response.ok){
        return response.json()
      }
    })
    .then((data)=>{
        if (data) {
          alert(data.message);
          localStorage.removeItem('token');
        }
    })
}


</script>

<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <RouterLink class="navbar-brand" to="/">Grocery Store</RouterLink>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item" v-if="!isAuthenticated()">
          <RouterLink class="nav-link active" aria-current="page" to="/login">Login</RouterLink>
        </li>
        <li class="nav-item" v-else>
          <button class="nav-link active" aria-current="page" @click="logout_user">Logout</button>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
</template>