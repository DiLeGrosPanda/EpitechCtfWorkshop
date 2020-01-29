<template>
  <div>
    <v-form
      ref="form"
      v-model="valid"
    >
      <v-text-field
        v-model="pseudo"
        :counter="1"
        :rules="pseudoRules"
        label="Pseudo"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        :rules="passwordRules"
        label="Password"
        required
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        color="success"
        @click="getResult"
      >Submit
      </v-btn>
    </v-form>
    {{ result }}
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    valid: false,
    pseudo: '',
    pseudoRules: [
      v => !!v || 'Pseudo is required',
      v => (v && v.length <= 1) || 'Pseudo must be less than 2 characters. Ha ha.'
    ],
    password: '',
    passwordRules: [
      v => !!v || 'Password is required',
    ],
    result: {}
  }),

  methods: {
    async getResult() {
      axios
        .get('/api/fakeLogin', { params: {
          pseudo: this.pseudo,
          password: this.password
        }})
        .then(res => { this.result = res.data })
        .catch(error => {this.result = error})
    }
  }
}
</script>
