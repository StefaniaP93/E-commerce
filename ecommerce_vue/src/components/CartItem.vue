<template>
    <tr>
        <td><router-link :to='item.product.get_absolute_url' class="text-dark">
            <strong>{{ item.product.name }}</strong>
        </router-link></td>
        <td>$ {{ item.product.price }}</td>
        <td>
            <button @click="decrementQuantity(item)" class="btn btn-sm btn-outline-secondary">-</button>
            <span class="ms-3 me-3">{{ item.quantity }}</span>
            <button @click="incrementQuantity(item)" class="btn btn-sm btn-outline-secondary">+</button>

        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="btn btn-secondary" @click="removeFromCart(item)">Delete</button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity -= 1
            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity += 1
            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item);
        },
    }
}
</script>