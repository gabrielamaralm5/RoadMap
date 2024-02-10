<template lang="">
  <form>
    <div id="container-form">
      <div>
        <label for="name">Nome do cliente:</label>
        <input
          name="name"
          id="name"
          type="text"
          placeholder="digite seu nome"
          class="down-element"
          required
        />
      </div>

      <div>
        <label for="pao">Escolha um pão:</label>
        <select name="pao" id="pao" class="down-element button-custo" >
          <option value="pao">Selecione Seu Pão</option>
          <option v-for="pao in paes" :value="pao.tipo" :key="pao.id">{{ pao.tipo }}</option>
        </select>
      </div>

      <div>
        <label for="meat" >Escolha Carne Do Seu Burge:</label>
        <select name="meat" id="meat" class="down-element button-custo" >
          <option value="meat">Selecione sua Carne</option>
          <option v-for="carne in carnes" :key="carne.id" :value="carne.tipo" required>
            {{ carne.tipo }}
          </option>
        </select>
      </div>

      <div class="option-checkbox" >
        <label for="checkbox">Selecione os opicionais:</label>
        <div id="checkbox-div" class="checkbox-uni" v-for="opicional in opicionais" :key="opicional.id">
          <input type="checkbox" name="checkbox"/>
          <span id="checkbox"> {{opicional.tipo}} </span>
        </div>

        
      </div><div id="submit">
          <button type="submit" class="submit">enviar</button>
        </div>
    </div>
  </form>
</template>
<script>
export default {
  name: 'formBurge',
  data() {
    return {
      paes: null,
      carnes: null,
      opicionais: null,
      nome: null,
      pao: null,
      carne: null,
      opicional: [],
      satus: 'solicitado',
      msg: null
    }
  },
  methods: {
    async GetIngredientes() {
      const req = await fetch('http://localhost:3000/ingredientes')
      const data = await req.json()

      this.paes = data.paes
      this.carnes = data.carnes
      this.opicionais = data.opcionais
      console.log('olA')
    }
  },
  mounted() {
    this.GetIngredientes()
  }
}
</script>
<style >
form {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 12px;
  margin: 12px;
}

#container-form {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 50px;
  width: 40%;
}

label {
  border-left: 5px solid yellow;
  padding: 10px;
}

.down-element {
  display: flex;
  flex-direction: row;
  position: relative;
  margin: 20px;
  width: 100%;
}
.option-checkbox {
  display: flex;
  justify-content: center;
  flex-direction: column;
}

#checkbox-div {
  margin: 20px;
}

#checkbox-div > input {
}

#name {
  background-color: aliceblue;
  border: 1px solid black;
  padding: 10px;
  width: 100%;
}

.button-custo {
  background-color: aliceblue;
  border: 1px solid black;
  padding: 10px;
  width: 100%;
}

.checkbox-uni > input,
span {
  padding: 10px;
  vertical-align: center;
}
.checkbox-uni > input {
  width: 20px;
  height: 20px;
}

.checkbox-uni > input:hover {
  width: 30px;
  height: 30px;
}

.submit {
  background-color: rgb(0, 0, 0);
  color: yellow;
  width: 100%;
  height: 100%;
  border: 0px;
}

#submit {
  background-color: black;
  width: 100%;
  height: 100%;
  padding: 10px;
  border-radius: 10px;
}
</style>
