import { createStore } from 'vuex'

export default createStore({
    state: {
        cart: {
            items: [],
        },
        isAuthenticated: false,
        token: '',
    },
    getters: {
    },
    mutations: {
        // Verifica se esiste già un carrello nell'archivio locale (localStorage) e lo carica nello stato se presente. 
        // In caso contrario, crea un nuovo carrello vuoto e lo salva nell'archivio locale.
        ///.parse è un metodo in JavaScript che viene utilizzato per analizzare una stringa JSON e convertirla in un oggetto JavaScript. JSON (JavaScript Object Notation) è un formato di dati testuali leggibile dall'uomo che rappresenta dati strutturati come oggetti JavaScript. 
        //È ampiamente utilizzato per la serializzazione e la trasmissione di dati tra un server e un client web, nonché per l'archiviazione di dati strutturati.
        //.stringify è un metodo in JavaScript utilizzato per convertire un oggetto JavaScript in una stringa JSON. 
        //Questo è utile quando si desidera serializzare un oggetto JavaScript in modo che possa essere memorizzato o trasmesso come stringa o quando si desidera inviare dati strutturati da un client a un server.
        initializeStore(state) {
            if (localStorage.getItem('cart')) {
                state.cart = JSON.parse(localStorage.getItem('cart'))
            } else {
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }

            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },


        //addToCart verifica se un carrello è gia esistente e ne carica i dati, altrimenti ne crea uno vuoto
        addToCart(state, item) {
            const exists = state.cart.items.filter(i => i.product.id === item.product.id)
            if (exists.length) {
                exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
            } else {
                state.cart.items.push(item)
            }

            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state, token) {
            state.token = ''
            state.isAuthenticated = false
        },
        clearCart(state) {
            state.cart = { items: [] }

            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
    },
    actions: {
    },
    modules: {
    }
})
