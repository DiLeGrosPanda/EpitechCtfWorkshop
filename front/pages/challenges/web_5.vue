<template>
  <div>
    <div v-if="answer === 'PROXY'">
      Flag{YouAreTheBest}
    </div>
    <div v-else>
      Expecting PROXY instead of {{ answer }}
    </div>
  </div>
</template>
<script>

import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  data: () => ({
    answer: ""
  }),
  mounted() {
    axios
      .get('/api/random')
      .then(res => { this.answer = res.data.content })
      .catch(error => {})
  }
}
</script>
