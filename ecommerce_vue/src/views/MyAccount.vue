<template>
    <div class="container mt-5">
        <h1>My Account</h1>
        <button @click="logout()" class="btn btn-danger">Logout</button>
    </div>
    <div class="mt-5">
        <h2 class="text-center text-primary mt-5">My orders</h2>
        <div class="mt-5" v-for="order in orders" v-bind:key="order.id" v-bind:order="order">
            <h4 class="mt-3 mb-6 text-secondary">Order #{{ order.id }}</h4>
            <table class="table table-fullwidth" v-if="orderTotalLength(order)">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in order.items" v-bind:key="item.product.id">
                        <td>{{ item.product.name  }}</td>
                        <td>${{ item.product.price }}</td>
                        <td>{{ item.quantity }}</td>
                        <td>${{ getItemTotal(item).toFixed(2) }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'MyAccount',
    props: {
        order: Object
    },
    data() {
        return {
            orders: []
        }
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            try {
                const response = await axios.get('/api/v1/orders/');
                this.orders = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        orderTotalLength(order) {
            return order.items.reduce((amount, item) => {
                return amount += item.quantity
            }, 0)
        }
    },
    mounted() {
        document.title = 'My Account | E-commerce'
        this.getMyOrders()
    }
}

</script>