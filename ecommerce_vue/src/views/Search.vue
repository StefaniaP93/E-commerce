<template>
    <div>
        <div class="container mt-5">
            <h2 class="mb-5">Search term: "{{ query }}"</h2>
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
    name: 'Search',
    data() {
        return {
            products: [],
            query: '',
        }
    },
    components: { ProductCard },
    mounted() {
        document.title = 'Search | E-Commerce';

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }
    },
    methods: {
        performSearch() {
            console.log(this.query)
            axios.post('/api/v1/products/search/', { 'query': this.query })
                .then(response => {
                    this.products = response.data
                }).catch(error => {
                    console.log(error.response.data)
                })
        }


    }
}
</script>