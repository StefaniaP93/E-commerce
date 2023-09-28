<template>
    <div class="container mt-5">
        <table class="table table-fullwidth">
            <thead>
                <tr>
                    <th scope="col">Name</th>
                    <th scope="col">Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Total</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in cart.items" v-bind:key="item.product.id">
                    <td>{{ item.product.name }}</td>
                    <td>$ {{ item.product.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td>Total</td>
                    <td>{{ cartTotalLength }}</td>
                    <td>${{ cartTotalPrice.toFixed(2) }}</td>
                </tr>
            </tfoot>
        </table>
        <div class="mt-5">
            <h2 class="subtitle">Shipping details</h2>
            <p class="text-secondary mb-4">* All fields are required</p>
            <div class="row">
                <div class="col">
                    <label>First name*</label>
                    <div class="control">
                        <input type="text" class="form-control input shadow rounded" v-model="first_name">
                    </div>
                    <label>Last name*</label>
                    <div class="control">
                        <input type="text" class="form-control input shadow rounded" v-model="last_name">
                    </div>
                    <label>E-mail*</label>
                    <div class="control">
                        <input type="email" class="form-control input shadow rounded" v-model="email">
                    </div>
                    <label>Phone*</label>
                    <div class="control">
                        <input type="text" class="form-control input shadow rounded" v-model="phone">
                    </div>
                </div>
                <div class="col">
                    <label>Address*</label>
                    <div class="control">
                        <input type="text" class="form-control input shadow rounded" v-model="address">
                    </div>
                    <label>CAP*</label>
                    <div class="control">
                        <input type="text" class="form-control input shadow rounded" v-model="cap">
                    </div>
                    <label>Place*</label>
                    <div class="control">
                        <input type="text" class="form-control input shadow rounded" v-model="place">
                    </div>
                    <div v-if="errors">
                        <div>
                            <p v-for="error in errors" v-bind:key="error" class="text-danger mt-1">{{ error }}</p>
                        </div>
                    </div>
                </div>
                <div id="card-element" class="mb-5 mt-5"></div>
            </div>
            <template v-if="cartTotalLength">
                <hr>
                <button class="btn btn-dark btn-lg" @click="submitForm">Pay</button>
            </template>

        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            cap: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Djackets'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51NuaJiG6N7VfEP8vaUiSpvwCbAJUMQ1C0u4wLGXARGdDc4hXlIPV3YZ9qhsixKOSRjfb612GrP3zh3NqesjXynEw00esJQk3d9')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []

            if (this.first_name === '') {
                this.errors.push('The First name is missing')
            }

            if (this.last_name === '') {
                this.errors.push('The Last name is missing')
            }

            if (this.email === '') {
                this.errors.push('The Email field is missing')
            }

            if (this.phone === '') {
                this.errors.push('The Phone field is missing')
            }

            if (this.address === '') {
                this.errors.push('The Address field is missing')
            }

            if (this.cap === '') {
                this.errors.push('The CAP field is missing')
            }

            if (this.place === '') {
                this.errors.push('The Place field is missing')
            }

            if (!this.errors.length) {
                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {
                        this.errors.push('Something went wrong with Stripe. Please try again')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const price = (item.product.price * item.quantity).toFixed(2);
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: parseFloat(price)
                }

                items.push(obj)
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'cap': this.cap,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')

                    console.log(error)
                })
        }
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
    }
}
</script>