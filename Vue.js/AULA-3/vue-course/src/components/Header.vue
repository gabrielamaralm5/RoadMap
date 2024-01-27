<template>
  <header>
    <div>
      <div 
      class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md flex items-center space-x-4"
      v-for="obj in todos"
      v-bind:key="obj.id"
      >
      {{ obj.title }}
      </div>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      todos:[
      {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  {
    "userId": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": false
  },
  {
    "userId": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": true
  },
  {
    "userId": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
    "completed": false
  },
      ]
    }
  }
}
</script>
<style>
header {
  background-color: black;
  color: white;
}
</style>
