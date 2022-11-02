<template>
  <div id="app" class="border">
    <h1> App </h1>
    <input type="text" v-model="appData">
    <p> parenetData: {{parentData}} </p>
    <p> childData: {{childData}} </p>

    <AppParent :app-data="appData" 
    @from-parent="fromParent"
    @from-child="fromChild"
    />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data(){
    return{
      appData:"",
      parentData:"",
      childData:"",
    }
  },  
    methods:{
    fromParent(pd){
      this.parentData = pd;
    },
    fromChild(cd){
      this.childData = cd;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border: solid 1px black;
}

</style>
