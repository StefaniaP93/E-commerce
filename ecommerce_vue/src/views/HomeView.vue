<template>
    <div class="home">
        <div class="container mt-5">
            <div class="row">
                <ProductCard v-for="product in products" v-bind:key="product.id" v-bind:product="product" />
                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ProductCard from "@/components/ProductCard.vue";

export default {
    name: 'HomeView',
    data() {
        return {
            products: []
        }
    },
    components: {
        ProductCard
    },
    mounted() {
        this.getProducts()
        document.title = 'Home | E-commerce'
    },
    methods: {
        getProducts() {
            axios.get('/api/v1/product/')
                .then(response => {
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}
</script>
<style scoped>
.image {
    margin-top: -1, 25 rem;
    margin-left: -1, 25 rem;
    margin-right: -1, 25 rem;
}
</style>
