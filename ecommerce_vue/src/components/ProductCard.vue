<template>
    <div class="col-12 col-md-3">
        <div class="card" style="width: 18rem;">
            <img v-bind:src="product.get_thumbnail" class="card-img-top image" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{ product.name }}</h5>
                <p class="card-text">{{ product.descrriptions }}</p>
                <p class="card-text">{{ product.price }}</p>
                <router-link v-bind:to="product.get_absolute_url" class="btn btn-secondary">View
                    details</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductCard',
    props: {
        product: Object
    }
}
</script>