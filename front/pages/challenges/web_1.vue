<template>
  <div>
    <div v-if="user_agent === 'Commodore 64'">
      Flag{YouAreSoGoodAtThisGameO_o}
    </div>
    <div v-else>
      I wish i were a Commodore 64...
      It was such a great time back then...
      <v-img
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Commodore-64-Computer-FL.jpg/1920px-Commodore-64-Computer-FL.jpg?1579559036662"
        :contain="true"
        max-height="400"
      ></v-img>
    </div>
  </div>
</template>
<script>

export default {
  async asyncData ({ req }){
    if (process.server) {
      return { user_agent: req.headers["user-agent"] }
    } else {
      // shouldn't happen as asyncData is called (once) server-side.. right?
      return { user_agent: false }
    }
  }
}
</script>
