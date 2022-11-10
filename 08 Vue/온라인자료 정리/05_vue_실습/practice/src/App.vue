<template>
  <div id="app">
    <h1> {{ title }} </h1>
    <h3> {{ subtitle }} </h3>

    📝<input type="text"
    @keyup.enter="insertTodo"
    v-model="inputTodo">📝

    <ul v-for="todo in todoList" :key="todo">
      <li>
        {{todo}}
      </li>
    </ul>

  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return{
      inputTodo: null, 
    }
  }
  ,
  computed:{
    title(){
      return this.$store.state.title
    },
    subtitle(){
      return this.$store.state.subtitle
    },
    todoList(){
      return this.$store.state.todolist
    }
  },
  methods:{
    insertTodo(){
      const todoData = this.inputTodo
      this.$store.dispatch('insertTodo', todoData)
      this.inputTodo = null
    }
  }


}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
