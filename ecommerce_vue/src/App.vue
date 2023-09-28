<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-dark bg-black">
            <div class="container-fluid">
                <a class="navbar-brand ms-4" href="/">E-commerce</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle ms-4" href="#" role="button" data-bs-toggle="dropdown">
                                <h6>Category</h6>
                            </a>
                            <ul class="dropdown-menu">
                                <li v-for="category in categories" :key="category.id">
                                    <router-link :to="category.get_absolute_url" class="dropdown-item">
                                        {{ category.name }}
                                    </router-link>
                                </li>
                            </ul>

                        </li>
                        <li class="nav-item">
                            <router-link to="/cart" class="btn btn-lg btn-outline-secondary ms-5">
                                <span class="icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-cart3" viewBox="0 0 16 16">
                                        <path
                                            d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .49.598l-1 5a.5.5 0 0 1-.465.401l-9.397.472L4.415 11H13a.5.5 0 0 1 0 1H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5zM3.102 4l.84 4.479 9.144-.459L13.89 4H3.102zM5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
                                    </svg>
                                </span>
                                <span class="small ms-1"> Cart ({{ cartTotalLength }})</span>
                            </router-link>
                        </li>
                    </ul>

                    <div class="navbar-item">
                        <form method="get" action="/search">
                            <div>
                                <div class="control">
                                    <input type="text" class="input" placeholder="What are you looking for?" name="query">
                                </div>

                                <div class="control">
                                    <button class="btn btn-success">Search</button>
                                </div>
                            </div>
                        </form>
                    </div>

                    <div class="navbar-item">
                        <div class="buttons">
                            <template v-if="$store.state.isAuthenticated">
                                <router-link to="/my-account" class="btn btn-primary">My Account</router-link>
                            </template>
                            <template v-else>
                                <router-link to="/log-in" class="btn btn-primary">Login</router-link>
                            </template>
                                                        
                        </div>

                    </div>
                </div>
            </div>
        </nav>
        <router-view />
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            isSearchVisible: false,
            cart: {
                items: [],
            },
            categories: []
        }
    },

    beforeCreate() {
        this.$store.commit('initializeStore');
        const token = this.$store.state.token

        if (token) {
            axios.defaults.headers.common['Authorization'] = "Token " + token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        this.getCategoryList()
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0;

            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity;
            }
            return totalLength;
        },
    },
    methods: {
        toggleSearch() {
            this.isSearchVisible = !this.isSearchVisible;
        },
        getCategoryList() {
            axios
                .get('/api/v1/categories')
                .then((response) => {
                    this.categories = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>

