import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    title: '✔️Todo List✔️',
    subtitle: '오늘은 어떤 사건이 날 기다릴까',
    todolist: [],

  },
  getters: {
  },
  mutations: {

    INSERT_TODO(state, todoData){
      state.todolist.push(todoData)
    }
  },
  actions: {
    insertTodo(context, todoData){
      context.commit('INSERT_TODO', todoData)
    }
  },
  modules: {
  }
})
