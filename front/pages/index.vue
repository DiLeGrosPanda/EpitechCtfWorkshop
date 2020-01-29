<template>
  <v-layout
    column
    justify-center
    align-center
  >
    <h2>Challenges</h2>

    <v-expansion-panels>
      <v-expansion-panel v-for="(type, categoryName) in challenges" :key="categoryName">
        <v-expansion-panel-header>{{ categoryName }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-card :color="validated.includes(chall.id) ? 'success' : 'transparent'" v-for="(chall, challName) in type" :key="challName">
            <v-card-title>{{ challName }}</v-card-title>
            <v-card-text v-if="!validated.includes(chall.id)">
              <v-layout column>
              <label>{{ chall.description }}</label>
              <v-btn
                text
                @click="startChall(chall)"
                left
              >Start the challenge !</v-btn>
              <v-form v-model="isFlag" @submit.prevent="" :lazy-validation="true">
                <v-text-field
                  label="flag"
                  :rules="[x => !!x && x === chall.flag || 'Invalid flag']"
                  v-model="chall.flag"
                ></v-text-field>
                <v-btn @click="checkFlag(categoryName, challName, chall)">Validate</v-btn>
              </v-form>
            </v-layout>
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
     <v-dialog v-model="dialog" max-width="290">
       <div>Invalid flag</div>
    </v-dialog>
  </v-layout>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'
import axios from 'axios'

export default {
  data: () => {
    return { dialog: false, isFlag: false }
  },
  async asyncData({ $axios }) {
    return await $axios.$get('/api/getChallenges')
  },
  computed: {
    validated: function () {
      return this.$store.state.completed
    }
  },
  methods: {
    checkFlag(categoryName, challName, chall) {
      console.log(categoryName, challName, chall.flag);
      axios.get('/api/checkFlag', {
        params: {categoryName: categoryName, challName: challName, flag: chall.flag }
      }).then(res => {
        console.log(res.data)
        if (res.data.isok) {
          this.$store.commit("completeChall", chall.id)
        } else {
          this.dialog = true
        }
      })
    },
    downloadFile(path) {
      var anchor = document.createElement('a');
      anchor.setAttribute('href', path);
      anchor.setAttribute('download', '');
      document.body.appendChild(anchor);
      anchor.click();
      anchor.parentNode.removeChild(anchor);
    },
    startChall(chall) {
      if (chall.to_dl) {
        this.downloadFile(chall.path);
      } else {
        this.$router.push(chall.path);
      }
    },
  }
}
</script>

<style>
.DONE {
  text-decoration: line-through;
}
</style>
