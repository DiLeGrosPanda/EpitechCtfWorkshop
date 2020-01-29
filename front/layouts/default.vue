<template>
  <v-app dark>

    <v-content>
      <v-container>
        <v-btn to="/">HOME</v-btn>
        <nuxt />
      </v-container>
    </v-content>

    <v-footer
      :fixed="true"
      app
    >
      <span>EPITECH Security Workshop by DiLeGrosPanda</span>
      <v-spacer></v-spacer>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
}
</script>
