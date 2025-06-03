<script setup>
import { ref } from 'vue';
import { defineProps} from 'vue';

const product = defineProps([
    'product_details',
    'key'
])

</script>


<template>
<div>
    <h1>List of all Products</h1>
    <p>{{product.product_details.name}}</p>

</div>

</template>