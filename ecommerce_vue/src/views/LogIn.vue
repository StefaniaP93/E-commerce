<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-12 text-center">
                <h1>LogIn</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input shadow rounded" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="text" class="input shadow rounded" v-model="password">
                        </div>
                    </div>
                    <div v-if="errors">
                        <div id="alerts">
                            <p v-for="error in errors" v-bind:key="error" class="text-danger mt-1">{{ error }}</p>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control mt-3">
                            <button class="btn btn-dark"><router-link to='/'>Login</router-link></button>
                        </div>
                        <hr>

                        Or <router-link to="/sign-up">click here</router-link> to sign up in!
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'E-commerce | LogIn'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')

                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>