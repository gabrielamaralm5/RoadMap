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
          <option value="pao">Integral</option>
        </select>
      </div>

      <div>
        <label for="meat">Escolha Carne Do Seu Burge:</label>
        <select name="meat" id="meat" class="down-element button-custo">
          <option value="meat">Selecione sua Carne</option>
          <option value="meat">maminha</option>
        </select>
      </div>

      <div class="option-checkbox">
        <label for="checkbox">Selecione os opicionais:</label>
        <div id="checkbox-div" class="checkbox-uni">
          <input type="checkbox" name="checkbox" />
          <span id="checkbox">salame</span>
        </div>

        <div id="checkbox-div" class="checkbox-uni">
          <input type="checkbox" name="checkbox" />
          <span id="checkbox">salame</span>
        </div>

        <div id="checkbox-div" class="checkbox-uni">
          <input type="checkbox" name="checkbox" />
          <span id="checkbox">salame</span>
        </div>
        <div id="submit">
      <button type="submit" class="submit">enviar</button>
    </div>
      </div>
      
    </div>

    
  </form>
</template>
<script>
export default {
  name: 'formBurge'
}
</script>
<style scoped>
form {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 50px;
  align-items: center;
  margin-bottom: 30px;
}

#container-form {
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
  border-radius:10px;
}
</style>
