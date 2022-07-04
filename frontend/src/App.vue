<template>
  <div id="main">
    <NavComponent />
    <ContentComponent />
    <FooterComponent />
  </div>
</template>

<script setup>
import NavComponent from './components/Nav.vue'
import ContentComponent from './components/Content.vue'
import FooterComponent from './components/Footer.vue'
</script>



<style>
#main {
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
  padding: 0;
  margin: 0;
}
</style>
