<template>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-10">
                <figure class="mb-4">
                    <img v-bind:src="product.get_image">
                </figure>
                <h1 class="display-4">{{ product.name }}</h1>
                <p class="lead">{{ product.description }}</p>
            </div>
            <div class="col-md-2">
                <h2 class="h4 mb-3">Information</h2>
                <p><strong>Price: </strong>${{ product.price }}</p>
                <div class="input-group mt-4">
                    <input type="number" class="form-control me-1" min="1" v-model="quantity">
                    <div class="input-group-append">
                        <div>
                            <button class="btn btn-dark" @click="addToCart()">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1,
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        getProduct() {
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug
            axios.get(`/api/v1/products/${category_slug}/${product_slug}/`)
                .then(response => {
                    this.product = response.data
                    document.title = this.product.name + ' | E-commerce'
                }).catch(error => {
                    console.log(error)
                })
        },

        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
        }
    },
}
</script>