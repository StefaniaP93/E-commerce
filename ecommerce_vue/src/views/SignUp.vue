<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-12 text-center">
                <h1>Sign-up</h1>
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
                    <div class="field">
                        <label>Repete password</label>
                        <div class="control">
                            <input type="text" class="input shadow rounded" v-model="password2">
                        </div>
                    </div>
                    <div v-if="errors">
                        <div id="alerts">
                            <p v-for="error in errors" v-bind:key="error" class="text-danger mt-1">{{ error }}</p>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control mt-3">
                            <button class="btn btn-dark">Sign up</button>
                        </div>
                        <hr>

                        Or <router-link to="/log-in">click here</router-link> to log in!
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'E-commerce | SignUp'
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }

                axios.post('/api/v1/users/', formData)
                    .then(response => {
                        this.showAlert('Account created, please log in!', 'alert-success');
                        this.$router.push('/log-in')
                    })

                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        },
        showAlert() {
            const alert = document.createElement('div');
            alert.className = `alert ${alertType} alert-dismissible fade show`;
            alert.role = 'alert';
            alert.innerHTML = `${message}
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                                </button>`;
            const alertsContainer = document.getElementById('alerts');
            alertsContainer.appendChild(alert);

            // Chiudi l'alert dopo 2 secondi (2000 millisecondi)
            setTimeout(() => {
                alert.classList.add('fade');
                setTimeout(() => {
                    alertsContainer.removeChild(alert);
                }, 500); // Tempo di animazione "fade"
            }, 2000); // Durata dell'alert
        }
    }
}

</script>

<style></style>