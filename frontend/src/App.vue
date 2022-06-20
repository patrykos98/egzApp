<template>
  <div id="app">
    <NavComponent />
    <ContentComponent />
    <FooterComponent />
  </div>
</template>

<script setup lang="ts">
import NavComponent from './components/Nav.vue'
import ContentComponent from './components/Content.vue'
import FooterComponent from './components/Footer.vue'
</script>



<!-- <style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->
