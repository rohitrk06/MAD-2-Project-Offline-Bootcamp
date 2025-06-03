<script setup>
import {defineProps} from 'vue';
import Products from './Products.vue';

const props = defineProps([
    'categories'
]);

</script>

<template>
<div>
    <h3>{{props.categories.name}}</h3>
    <Products v-for="product in props.categories.products" :product_details="product" :key="'1'" />


</div>
</template>