<template>
    <div class="mt-4">
        <table class="table table-fullwidth" v-if="cartTotalLength">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>
            <tbody>
                <CartItem 
                v-for="item in cart.items" 
                v-bind:key="item.product.id" 
                v-bind:initialItem="item" 
                v-on:removeFromCart="removeFromCart" />
                
            </tbody>


        </table>
        <p v-else class="mt-5">You don't have any products in your cart...</p>
            </div>

            <div class="col-12 mt-4">
                <h2 class="subtitle mt-3">Summary</h2>

                <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

                <hr>

                <router-link to="/cart/checkout" class="btn btn-dark">Proceed to checkout</router-link>
    </div>
</template>

<script>
import CartItem from "@/components/CartItem.vue";
import axios from 'axios'


export default {
    name: 'Cart',
    components: 'CartItem',
    data() {
        return {
            cart: {
                items: []
            }
        };
    },
    components: {
        CartItem
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((amount, item) => {
                return amount += item.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((total, item) => {
                return total += item.product.price * item.quantity
            }, 0)
        }
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    }
}


</script>