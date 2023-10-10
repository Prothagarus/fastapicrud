<script lang="ts">
import { defineComponent } from 'vue';
import { TabulatorFull as Tabulator } from 'tabulator-tables';
import { DateTime, Settings } from 'luxon';
import { type RowComponent, type CellComponent } from 'tabulator-tables';
import 'tabulator-tables/dist/css/tabulator.min.css'
import 'tabulator-tables'
import 'flatpickr'
import 'flatpickr/dist/flatpickr.css'
import 'flatpickr/dist/themes/material_blue.css';
import 'luxon'
import 'moment'
import VueDatePicker from '@vuepic/vue-datepicker';
import 'vuetify'
interface ToDoGet {
    id: string;
    task: string;
    startdate: DateTime;
    enddate: DateTime;
}

interface Taskdropdown {
    task: string;
}

export default defineComponent({
    data() {
        return {
            tabulator: null,
            tableData: [] as Array<ToDoGet>,
            taskdropdown: [] as Array<Taskdropdown>,
            savedata: [] as Array<ToDoGet>
        };
    },
    methods: {
        gettabledata() {
            fetch('http://localhost:8043/ToDoGet')
                .then((d) => d.json())
                .then((d2: Array<ToDoGet>) => {
                    this.tableData.push(...d2);
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },
        // gettabledata() {
        //     this.tableData = [];
        //     fetch('http://localhost:8043/ToDoGet').then((d) => d.json().then((d2: Array<ToDoGet>) => { this.tableData = d2; }));
        // },
        getdropdownlist() {
            this.taskdropdown = [];
            fetch('http://localhost:8043/ToDo_DropdownList').then((d) => d.json().then((d2: Array<Taskdropdown>) => { this.taskdropdown = d2; }));
        },
        persisttablechangestobuffer(row: RowComponent) {
            this.savedata.push(row.getData());
        },
        // other methods...

        addNewRow() {
            const newRow = {
                id: '', // You might want to generate a unique ID here
                task: this.taskdropdown[0]?.task || 'uncategorized',
                startdate: DateTime.local(),
                enddate: DateTime.local(),
            };
            //this.tableData.push(newRow);
            this.tabulator.addRow(newRow);
            this.savedata.push(newRow);
        },
        flatpickrEditor(cell, onRendered, success, cancel) {
            // create and style input
            var cellValue = DateTime.fromISO(cell.getValue()).toFormat("yyyy-MM-dd'T'HH:mm:ss");
            var input = document.createElement("input");
            input.style.width = "100%";
            input.style.height = "100%";
            input.value = cellValue;

            onRendered(function () {
                flatpickr(input, {
                    enableTime: true,
                    dateFormat: "Z",//Z is dateformat for ISO in flatpickr options

                    defaultDate: cellValue,
                    onClose: (selectedDates, dateStr, instance) => {
                        success(dateStr);
                        instance.destroy();
                    },
                    onChange: function (selectedDates, dateStr, instance) {
                        success(dateStr);
                        instance.destroy();
                    },
                });
            });

            //return the input element
            return input;
        },
        sendData() {
            fetch('http://localhost:8043/ToDo_Save', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.savedata),
            })
                .then((response) => response.json())
                .then((data) => {
                    console.log('Success:', data);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        },
    },
    mounted() {
        this.gettabledata();
        this.getdropdownlist();

        this.tabulator = new Tabulator(this.$refs.table, {

            data: this.tableData,
            reactiveData: true,
            columns: [
                //{ title: 'id', field: 'id' },
                {
                    title: 'task',
                    field: 'task',
                    editor: "select",
                    editorParams: () => {
                        let dropdownOptions = {};
                        this.taskdropdown.forEach((option) => {
                            dropdownOptions[option.task] = option.task;
                        });
                        return { values: dropdownOptions };
                    }
                },
                {
                    title: 'Start Date',
                    field: 'startdate',
                    sorter: 'datetime',
                    //sorterParams: { format: "yyyy-MM-dd HH:mm:ss" },
                    editor: this.flatpickrEditor,
                    formatter: (cell) => DateTime.fromISO(cell.getValue()).toFormat("yyyy-MM-dd HH:mm:ss")

                },
                {
                    title: 'End Date',
                    field: 'enddate',
                    sorter: 'datetime',
                    //sorterParams: { format: "yyyy-MM-dd HH:mm:ss" },
                    editor: this.flatpickrEditor,
                    formatter: (cell) => DateTime.fromISO(cell.getValue()).toFormat("yyyy-MM-dd HH:mm:ss")
                },


            ],
            cellEdited: (cell) => {
                this.persisttablechangestobuffer(cell.getRow());
            }
        });
    }
});
</script>

<template>
    <button @click="addNewRow">Add New Row</button>
    <button @click="sendData">Save Data</button>
    <div ref="table"></div>
</template>