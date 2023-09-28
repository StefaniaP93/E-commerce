<template>
    <div class="container mt-5">
        <h2>Thank you!</h2>
        <p>Your order will be processed within 48 hours.</p>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Success | E-commerce'
    }
}
</script>