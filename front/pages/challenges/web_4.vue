<template>
  <v-container>
    <v-layout row>
      <v-flex>
      </v-flex>
      <v-flex>
        <h1>What will it be ?</h1>
        <v-select
          v-model="choice"
          :items="category"
          filled
          label="Food"
        ></v-select>
        <v-btn @click=loadData()>Tell me more !</v-btn>
        <p></p>
        <v-card v-for="(item, i) in items" :key="i">
          <v-img class="white--text align-end" :height="300" :contain=true :src="item.food_link">
            <v-card-title>{{ item.food_name }}</v-card-title>
          </v-img>
          <v-card-text class="text--primary">{{ item.food_desc }}</v-card-text>
          <v-card-actions>
            <v-btn color="orange" text>Commander</v-btn>
          </v-card-actions>
        </v-card>
        <v-spacer></v-spacer>
      </v-flex>
      <v-flex>
      </v-flex>

    </v-layout>
  </v-container>
</template>
<script>
import axios from 'axios'

export default {
  data: () => ({
    category: [ "Pizza", "Kebab", "Raclette" ],
    items: [],
    choice: 0
  }),
  mounted() {
    this.loadData()
  },

  methods: {
    async loadData() {
      axios
        .get('/api/foods2', { params: { id: this.category.indexOf(this.choice) + 1 } })
        .then(res => { this.items = res.data })
        .catch(error => { console.log(error) })
      console.log("done")
    }
  },
}
</script>

