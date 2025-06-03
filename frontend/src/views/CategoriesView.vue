<script setup>
import Categories from '../components/Categories.vue';
import { ref } from 'vue';

const categories = ref([
    {
        "id":1,
        "name":"Electronics",
        "products":[
            {
                "id":1,
                "name":"Smartphone",
                "price":699.99,
            },
            {
                "id":2,
                "name":"Laptop",
                "price":1299.99,
            },
            {
                "id":3,
                "name":"Smartwatch",
                "price":199.99,
            }
        ]
    },
    {
        "id":2,
        "name":"Home Appliances",
        "products":[
            {
                "id":4,
                "name":"Refrigerator",
                "price":899.99,
            },
            {
                "id":5,
                "name":"Washing Machine",
                "price":499.99,
            },
            {
                "id":6,
                "name":"Microwave Oven",
                "price":199.99,
            }
        ]
    },
    {
        "id":3,
        "name":"Furniture",
        "products":[
            {
                "id":7,
                "name":"Sofa",
                "price":799.99,
            },
            {
                "id":8,
                "name":"Dining Table",
                "price":599.99,
            },
            {
                "id":9,
                "name":"Bed Frame",
                "price":699.99,
            }
        ]
    }
]) 


</script>

<template>
    <div>
        <h1>List of all Categories</h1>
        <Categories v-for="category in categories" :categories = category />
    </div>
</template>