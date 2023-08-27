<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <v-toolbar dense>
    <v-toolbar-title>Application</v-toolbar-title>
    <v-btn
      variant="outlined"
      @click="$router.push('/')"
    >Home</v-btn>
    <v-btn
      variant="outlined"
      @click="$router.push('/add')"
    >Add</v-btn>
    <v-btn
      variant="outlined"
      @click="$router.push('/query')"
    >Query</v-btn>
    
    <v-spacer></v-spacer>
  </v-toolbar>
  <RouterView></RouterView>
</template>

<style scoped>
</style>