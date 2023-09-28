<template>
    <div class="container mt-5">
        <h1 class="text-center"> {{ category.name }}</h1>
        <div class="row mt-5">
            <div class="col-12 col-md-4" v-for="product in category.products" v-bind:key="product.id">
                <div class="card" style="width: 18rem;">
                    <img v-bind:src="product.get_thumbnail" class="card-img-top image" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text">{{ product.descrription }}</p>
                        <p class="card-text">$ {{ product.price }}</p>
                        <router-link v-bind:to="product.get_absolute_url" class="btn btn-secondary mt-4">View
                            details</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Category',
    data() {
        return {
            category: {
                products: []
            }
        }
    },
    watch: {
        '$route': 'getCategory' // Osserva il cambiamento nell'URL e richiama getCategory
    },
    mounted() {
        this.getCategory()
    },
    methods: {
        getCategory() {
            const categorySlug = this.$route.params.category_slug
            axios.get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data
                    document.title = this.category.name + ' | E-commerce'
                }).catch(error => {
                    console.log(error)
                })

        }
    }
}
</script>